from typing import Optional, Any
from pydantic import BaseModel


class AuthResponse(BaseModel):
    class User(BaseModel):
        userId: Optional[int] = None
        email: Optional[str] = None
        countryCode: str = "US"
        fullName: Optional[str] = None
        firstName: Optional[str] = None
        lastName: Optional[str] = None
        nickname: Optional[str] = None
        username: Optional[str] = None
        address: Optional[str] = None
        city: Optional[str] = None
        postalcode: Optional[str] = None
        usState: Optional[str] = None
        phoneNumber: Optional[str] = None
        birthday: Optional[Any] = None
        channelId: Optional[int] = None
        parentId: Optional[int] = None
        acceptedEULA: Optional[bool] = None
        created: Optional[Any] = None
        updated: Optional[Any] = None
        facebookUid: Optional[Any] = None
        appleUid: Optional[Any] = None
        googleUid: Optional[Any] = None
        accountLinkCreated: Optional[bool] = None
        emailVerified: Optional[bool] = None
        newUser: Optional[bool] = None

    user: User
    scope: Optional[str] = None
    clientName: Optional[str] = None
    token_type: Optional[str] = None
    access_token: str
    expires_in: int
    user_id: int


class AuthResponseWithRefresh(AuthResponse):
    refresh_token: str


class AuthDeviceResponse(BaseModel):
    deviceCode: str
    userCode: str
    verificationUri: str
    verificationUriComplete: str
    expiresIn: int
    interval: int
