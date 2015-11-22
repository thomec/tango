# lists/tests/test_views.py

from unittest import skip

from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.utils.html import escape

from lists.views import home_page
from lists.models import Item, List
from lists.forms import EMPTY_ITEM_ERROR, ItemForm

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 2, 3)


class HomePageTest(TestCase):
    maxDiff = None

    def test_root_url_resolves_to_home_page_view(self):         # to be deleted
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):              # to be deleted
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('lists/home.html', {'form': ItemForm()})
        # self.assertEqual(response.content.decode(), expected_html)
        self.assertMultiLineEqual(response.content.decode(), expected_html)


    def test_home_page_only_saves_items_when_necessary(self):   # to be deleted
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)
        
        
    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')


    def test_home_page_uses_item_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], ItemForm)
        
        
class ListViewTest(TestCase):

    def post_invalid_input(self):
        list_ = List.objects.create()
        return self.client.post(
            '/lists/%d/' % (list_.id,),
            data={'text': ''}
        )


    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/' % (list_.id,))
        self.assertTemplateUsed(response, 'lists/list.html')


    def test_displays_only_items_for_this_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)

        response = self.client.get('/lists/%d/' % (correct_list.id,))

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')


    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id,))
        self.assertEqual(response.context['list'], correct_list)


    def test_can_save_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'text': 'A new item for an existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)


    def test_post_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            '/lists/%d/' % (correct_list.id,),
            data={'text': 'A new item for an existing list'}
        )

        self.assertRedirects(response, '/lists/%d/' % (correct_list.id,))
        
    @skip    
    def test_validation_errors_end_up_on_lists_page(self): # to be deleted
        list_ = List.objects.create()
        response = self.client.post(
            '/lists/%d/' % (list_.id,),
            data={'text': ''}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/list.html')
        expected_error = escape("You can't have an empty list item!")
        self.assertContains(response, expected_error)


    def test_displays_item_form(self):
        list_ = List.objects.create()
        response = self.client.get('/lists/%d/' % (list_.id,))
        self.assertIsInstance(response.context['form'], ItemForm)
        self.assertContains(response, 'name="text"')


    def test_for_invalid_input_nothing_saved_to_db(self):
        self.post_invalid_input()
        self.assertEqual(Item.objects.count(), 0)

    def test_for_invalid_input_renders_list_template(self):
        response = self.post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/list.html')

    def test_for_invalid_input_passes_form_to_template(self):
        response = self.post_invalid_input()
        self.assertIsInstance(response.context['form'], ItemForm)

    def test_for_invalid_input_shows_error_on_page(self):
        response = self.post_invalid_input()
        self.assertContains(response, escape(EMPTY_ITEM_ERROR))



class NewListTest(TestCase):

    def test_saving_post_request(self):
        self.client.post('/lists/new', data={'text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')


    def test_redirect_after_post(self):
        response = self.client.post(
                '/lists/new', data={'text': 'A new list item'}
                )
        new_list = List.objects.first()
        self.assertRedirects(response, '/lists/%d/' % (new_list.id,))
        
    @skip
    def test_validation_errors_are_sent_back_to_home_page_template(self): # to be deleted
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertEqual(response.status_code, 200)                     # test_for_invalid_input_renders_home_page
        self.assertTemplateUsed(response, 'lists/home.html')            # test_for_invalid_input_renders_home_page
        expected_error = escape("You can't have an empty list item!")   # -> You can&#39;t
        self.assertContains(response, expected_error)
    
    
    def test_invalid_list_items_arent_saved(self):
        self.client.post('/lists/new', data={'text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)


    def test_for_invalid_input_renders_home_template(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lists/home.html')


    def test_validation_errors_are_shown_on_home_page(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertContains(response, escape(EMPTY_ITEM_ERROR))


    def test_for_invalid_input_passes_form_to_template(self):
        response = self.client.post('/lists/new', data={'text': ''})
        self.assertIsInstance(response.context['form'], ItemForm)




