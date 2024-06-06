"""Base script used across defined."""

import requests
import paystackpy

class Borg:
    """
    Borg class making class attributes global.
    Implements the Borg design pattern which allows all instances to share state.
    """
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Base(Borg):
    """
    Base Class used across defined.
    This class initializes the Paystack API with the provided secret key.
    
    Attributes:
        requests (PayStackRequests): An instance of the PayStackRequests class for making API requests.
    """

    def __init__(self, **kwargs):
        """
        Initialize Paystack with secret key.

        Keyword Args::
            secret_key (str, optional): Paystack secret key. If not provided, uses the default from paystackpy.
            authorization (str, optional): Authorization header. If not provided, it is constructed using the secret key.
        """
        super().__init__()
        secret_key = kwargs.get('secret_key', paystackpy.SECRET_KEY)
        authorization = kwargs.get(
            'authorization',
            f"{paystackpy.HEADERS['Authorization'].format(secret_key)}"
        )
        headers = {'Authorization': authorization}
        arguments = {'api_url': paystackpy.BASE_API_URL, 'headers': headers}
        
        if not hasattr(self, 'requests'):
            req = PayStackBaseRequests(**arguments)
            self._shared_state.update(requests=req)


class PayStackBaseRequests:
    """
    Handles HTTP requests to the Paystack API.
    
    Args:
        api_url (str): The base URL for the Paystack API.
        headers (dict): A dictionary of headers to include in the requests.
    """

    def __init__(self, api_url=paystackpy.BASE_API_URL, headers=None):
        self.BASE_API_URL = api_url
        self.headers = headers

    def _request(self, method, resource_uri, **kwargs):
        """
        Perform a HTTP request on a resource.

        Args:
            method (function): HTTP method from requests (e.g., requests.get, requests.post).
            resource_uri (str): The endpoint of the resource.

        Keyword Args:
            data (dict, optional): JSON data to send in the body of the request.
            params (dict, optional): Query parameters to include in the URL.
            headers (dict, optional): Additional headers to include in the request.

        Raises:
            HTTPError: If the HTTP request returns an unsuccessful status code.

        Returns:
            dict: The JSON response from the API.
        """
        data = kwargs.get("data")
        params = kwargs.get("params")
        headers = kwargs.get("headers")
        
        if headers is not None:
            headers.update(self.headers)
        else:
            headers = self.headers
            
        response = method(
            self.BASE_API_URL + resource_uri,
            json=data,
            headers=headers,
            params=params
        )
        response.raise_for_status()
        return response.json()

    def get(self, endpoint, **kwargs):
        """
        Send a GET request to a resource.

        Args:
            endpoint (str): The endpoint of the resource.

        Keyword Args:
            params (dict, optional): Query parameters to include in the URL.

        Returns:
            dict: The JSON response from the API.
        """
        return self._request(requests.get, endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        """
        Send a POST request to create a resource.

        Args:
            endpoint (str): The endpoint of the resource.
        
        Keyword Args:
            data (dict, optional): JSON data to send in the body of the request.

        Returns:
            dict: The JSON response from the API.
        """
        return self._request(requests.post, endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        """
        Send a PUT request to update a resource.

        Args:
            endpoint (str): The endpoint of the resource.
        
        Keyword Args:
            data (dict, optional): JSON data to send in the body of the request.

        Returns:
            dict: The JSON response from the API.
        """
        return self._request(requests.put, endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        """
        Send a DELETE request to remove a resource.

        Args:
            endpoint (str): The endpoint of the resource.

        Keyword Args:
            params (dict, optional): Query parameters to include in the URL.
            headers (dict, optional): Additional headers to include in the request.

        Returns:
            dict: The JSON response from the API indicating the result of the delete operation.

        Raises:
            HTTPError: If the HTTP request returns an unsuccessful status code.
        """
        return self._request(requests.delete, endpoint, **kwargs)
