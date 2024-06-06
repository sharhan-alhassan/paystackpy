"""Script used to define the Paystack Customer class."""

from paystackpy.base import Base

class Customer(Base):
    """
    Customer class for interacting with Paystack's Customer API.

    This class provides methods to create, retrieve, list, and update customers
    using the Paystack API. Each method communicates with a specific endpoint
    of the Paystack API to perform the corresponding action.

    Attributes:
        None
    """

    @classmethod
    def create(cls, **kwargs):
        """
        Create a new customer on Paystack.

        Args:
            first_name (str): Customer's first name.
            last_name (str): Customer's last name.
            email (str): Customer's email address.
            phone (str): Customer's phone number.

        Returns:
            dict: JSON data from Paystack API containing the details of the created customer.
        """
        return cls().requests.post('customer', data=kwargs)

    @classmethod
    def get(cls, customer_id):
        """
        Retrieve a customer's details by their Paystack ID.

        Args:
            customer_id (str): Paystack customer ID.

        Returns:
            dict: JSON data from Paystack API containing the customer's details.
        """
        return cls().requests.get(f"customer/{customer_id}")

    @classmethod
    def list(cls, **kwargs):
        """
        List all customers on Paystack, with optional filtering and pagination.

        Args:
            perPage (int, optional): Specify how many records you want to retrieve per page.
                                     Defaults to 50 if not specified.
            page (int, optional): Specify exactly which page you want to retrieve.
                                  Defaults to 1 if not specified.
            from (str, optional): A timestamp from which to start listing customers.
                                  e.g. "2016-09-24T00:00:05.000Z" or "2016-09-21".
            to (str, optional): A timestamp at which to stop listing customers.
                                e.g. "2016-09-24T00:00:05.000Z" or "2016-09-21".

        Returns:
            dict: JSON data from Paystack API containing the list of customers.
        """
        return cls().requests.get('customer', params=kwargs)

    @classmethod
    def update(cls, customer_id, **kwargs):
        """
        Update an existing customer's details by their Paystack ID.

        Args:
            customer_id (str): Paystack customer ID.
            first_name (str, optional): Customer's first name.
            last_name (str, optional): Customer's last name.
            email (str, optional): Customer's email address.
            phone (str, optional): Customer's phone number.

        Returns:
            dict: JSON data from Paystack API containing the updated customer's details.
        """
        return cls().requests.put(f"customer/{customer_id}", data=kwargs)
