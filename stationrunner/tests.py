from django.test import TestCase
from django.core.urlresolvers import reverse


class TestStationCreate(TestCase):
    def test_page_exists(self):
        """
        Tests if a page exists for creation of station
        """
        response = self.client.get(reverse("createstation"))
        assert response.status_code == 200
    def test_contains_required_fields(self):
        """
        Tests if the page for creation of a station contains a form and
        the required fields
        """
        response = self.client.get(reverse("createstation"))
        assert "form" in response.context
        assert "name" in response.content
        assert "address" in response.content
    def test_submission_form_creates_station_object(self):
        """
        Tests if submission of the form on page for creation of a 
        station creates a station object and its attributes take the 
        submitted values
        """
        name = "examplename"
        address = "exampleaddress"
        response = self.client.post(reverse("createstation"),
                                    {"name": name, "address": address},
                                    follow=True)
        assert "station" in response.context
        s = response.context["station"]
        assert s.name == name
        assert s.address == address

class TestStationEdit(TestCase):
    def test_page_exists(self):
        """
        Tests if a page exists for editing a created station
        """
        name = "examplename"
        address = "exampleaddress"
        response = self.client.post(reverse("createstation"),
                                    {"name": name, "address": address},
                                    follow=True)
        s = response.context["station"]
        response_two = self.client.get(reverse("editstation", kwargs={'id':s.id}))
        assert response_two.status_code == 200  
    
    def test_contains_required_fields(self):
        """
        Tests if the page for editing a station contains a form and
        the required fields containing values from the station object to be 
        edited
        """
        name = "examplename"
        address = "exampleaddress"
        response = self.client.post(reverse("createstation"),
                                    {"name": name, "address": address},
                                    follow=True)
        s = response.context["station"]
        response_two = self.client.get(reverse("editstation", kwargs={'id':s.id}))
        assert "form" in response_two.context
        assert s.name in response_two.content
        assert s.address in response_two.content
        
    def test_submission_form_edits_station_object(self):
        """
        Tests if submission of the form on page for editing an
        existing station object saves the object into db with the
        attributes overwritten with the new values.
        """
        name = "examplename"
        address = "exampleaddress"
        response = self.client.post(reverse("createstation"),
                                    {"name": name, "address": address},
                                    follow=True)
        s = response.context["station"]
        response_two = self.client.get(reverse("editstation", kwargs={'id':s.id}))                            
        response_three = self.client.post(reverse("editstation", kwargs={'id':s.id}),
                                          {"name": "editedname", "address": "editedaddress"},
                                          follow=True)
        edited_s = response_three.context["station"]
        assert edited_s.name == "editedname"
        assert edited_s.address == "editedaddress"
        assert s.id == edited_s.id

class TestListStations(TestCase):
    def test_page_exists(self):
        """
        Checks if a page exists at the desired URL for listing all the
        stations.
        """
        response = self.client.get(reverse("liststations"))
        assert response.status_code == 200
        
