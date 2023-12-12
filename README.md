# Vendor Management System with Performance Metrics

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                   ********very Important**********
      please make sure not skip line 68 and 132  of this text file

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
## Overview

This project implements a Vendor Management System using Django and Django REST Framework. The system includes features for managing vendor profiles, tracking purchase orders, and calculating vendor performance metrics.

## Features

- **Vendor Profile Management:**
  - Create, retrieve, update, and delete vendor profiles.
- **Purchase Order Tracking:**
  - Create, retrieve, update, and delete purchase orders.
- **Vendor Performance Evaluation:**
  - Calculate and retrieve vendor performance metrics.
- **Purchase Order Acknowledgement:**
  - can update acknowledgment time.

## Getting Started

### Prerequisites

- Python 3.6+
- Django
- Django RestFrameWork  
- Pip
- Virtualenv (optional but recommended)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/vinaychitirala/FatMug.git
    cd vendor-management-system
    ```

2. Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

The API should now be accessible at `http://127.0.0.1:8000/`.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#####
please make sure that you are applying migrations only once if you had applied migrations more than once please make sure that """" UniqueCode """" Model has only two records if there are more than two record (name="Vendor" ,code="1000"and name = "Po",code="100") please remove the records from that particular table else the code will run into errors 
####
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

## API Endpoints

- **Vendor Endpoints:**
  - POST `/api/vendors/`: Create a new vendor.
  - GET `/api/vendors/`: List all vendors.
  - GET `/api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
  - PUT `/api/vendors/{vendor_id}/`: Update a vendor's details.
  - DELETE `/api/vendors/{vendor_id}/`: Delete a vendor.

- **Purchase Order Endpoints:**
  - POST `/api/purchase_orders/`: Create a purchase order.
  - GET `/api/purchase_orders/`: List all purchase orders with an option to filter by vendor.
  - GET `/api/purchase_orders/{po_id}/`: Retrieve details of a specific purchase order.
  - PUT `/api/purchase_orders/{po_id}/`: Update a purchase order.
  - DELETE `/api/purchase_orders/{po_id}/`: Delete a purchase order.

- **Vendor Performance Endpoint:**
  - GET `/api/vendors/{vendor_id}/performance`: Retrieve a vendor's performance metrics.

- **Update Acknowledgment Endpoint:**
  - POST `/api/purchase_orders/{po_id}/acknowledge`: Acknowledge a purchase order.

## Backend Logic for Performance Metrics

- **On-Time Delivery Rate:**
  - Calculated each time a PO status changes to 'completed'.
  - Logic: Count the number of completed POs delivered on or before delivery_date and divide by the total number of completed POs for that vendor.

- **Quality Rating Average:**
  - Updated upon the completion of each PO where a quality_rating is provided.
  - Logic: Calculate the average of all quality_rating values for completed POs of the vendor.

- **Average Response Time:**
  - Calculated each time a PO is acknowledged by the vendor.
  - Logic: Compute the time difference between issue_date and acknowledgment_date for each PO, and then find the average of these times for all POs of the vendor.

- **Fulfillment Rate:**
  - Calculated upon any change in PO status.
  - Logic: Divide the number of successfully fulfilled POs (status 'completed' without issues) by the total number of POs issued to the vendor.

## Additional Technical Considerations

- **Efficient Calculation:**
  - Ensure that the logic for calculating metrics is optimized to handle large datasets without significant performance issues.

- **Data Integrity:**
  - Include checks to handle scenarios like missing data points or division by zero in calculations.

- **Real-time Updates:**
  - Consider using Django signals to trigger metric updates in real-time when related PO data is modified.

## Technical Requirements

- **Django Version:** 3.2 (latest stable)
- **Django REST Framework Version:** 3.12 (latest stable)
- **Database:** SQLite (default in Django)
- **Authentication:** Token-based authentication
- **Coding Style:** PEP 8

## Testing
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
before executing test suite make sure that signals.py file code is not commented from line 7 to 11
if you wish to comment that particular code  make sure to craete objects for unique code model in setUp method of each class in tests.py

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
To run the test suite, use the following command:

```bash for windows

****please navigate to MyProject Directory and run the following command

 python manage.py test vms


#Authorization
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Token Authorization is required for each api to be accessible 
Token are meant to be created from Django Admin Panel for each user

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
