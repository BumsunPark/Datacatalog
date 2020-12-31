import os
import boto3


def get_username():
    return os.getlogin()


def get_secretkey():
    return os.getenv('SecretKey')


def is_valid_user():
    return True


def load_dynamodb_catalog():
    catalog = [
        {'Data name': 'defect_inspection'}, {'Description': ''}, {'Column list': ['a', 'b', 'c']}, {'Accessible': 'Y'}
    ]
    return catalog


def load_s3_catalog():
    catalog = [
        {'Data name': 'defect_inspection'}, {'Description': ''}, {'Column list': ['a', 'b', 'c']}, {'Accessible': 'Y'}
    ]
    return catalog
