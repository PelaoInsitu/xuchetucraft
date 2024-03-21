import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from settings import APP_CREDENTIALS, APP_TOKEN
from google.oauth2 import service_account


class GoogleDriveAuth:
    #If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

    ##Autenticación con API de Google Drive
    #@classmethod
    #def authenticate(cls):
    #    creds = None
    #    # The file token.json stores the user's access and refresh tokens, and is
    #    # created automatically when the authorization flow completes for the first
    #    # time.
    #    if os.path.exists(APP_TOKEN):
    #        creds = Credentials.from_authorized_user_file(APP_TOKEN, cls.SCOPES)
    #    # If there are no (valid) credentials available, let the user log in.
    #    if not creds or not creds.valid:
    #        if creds and creds.expired and creds.refresh_token:
    #            creds.refresh(Request())
    #        else:
    #            flow = InstalledAppFlow.from_client_secrets_file(
    #            APP_CREDENTIALS, cls.SCOPES
    #      )
    #            creds = flow.run_local_server(port=0)
    #    # Save the credentials for the next run
    #    with open(APP_TOKEN, "w") as token:
    #      token.write(creds.to_json())

    #    return creds
    

    #Autenticación con cuenta de servicio
    @classmethod
    def authenticate2(cls):
        credentials = service_account.Credentials.from_service_account_file(APP_CREDENTIALS,scopes=cls.SCOPES)

        return credentials