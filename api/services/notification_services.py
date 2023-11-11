import pip._vendor.requests as req

from api.models.profile import Profile


class NotificationService:
    
    def send_notification(profile: type[Profile], message: str):
        data = {
            'email': profile.email,
            'message': message,
        }
        r = req.post("https://run.mocky.io/v3/54dc2cf1-3add-45b5-b5a9-6bf7e7f1f4a6", data=data)
        
        if not r.status_code == 200:
            print('erro aou enviar a notificação')
            raise Exception("Serviço de notificação está fora do ar")
        
        