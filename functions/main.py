from functions_framework import http
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import logging

@http
def resume_fetch(request):
    """
    HTTP Cloud Function to fetch resume data from Firestore for a specific document.
    """

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Initialize Firebase Admin SDK
    cred = credentials.Certificate('nitish-resume-api-cloud-firebase-adminsdk-53s4h-7a2db2226b.json')
    try:
        firebase_admin.initialize_app(cred)
    except firebase_admin.exceptions.Error as e:
        logger.exception("Error initializing Firebase Admin: %s", e.args[0])
        return "Error initializing Firebase Admin", 500

    # Access Firestore
    db = firestore.client()
    resume_collection = db.collection('resume-1')

    try:
        # Fetch the specific document
        document = resume_collection.document('WYE9gU69t6Tjt4Je6XzM').get()

        if document.exists:
            data = document.to_dict()
            nitish_resume = data.get('nitish')
            return json.dumps(nitish_resume, indent=4)
        else:
            logger.error('Document not found: WYE9gU69t6Tjt4Je6XzM')
            return "No document found for document ID: WYE9gU6XzM", 404
    except Exception as e:
        logger.exception("Error fetching data: %s", e)
        return "An error occurred", 500

