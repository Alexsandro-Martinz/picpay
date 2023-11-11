from decimal import Decimal
import pip._vendor.requests as req
from api.models.profile import Profile


class TransactionService:
    
    def authorize_trasaction(sender_profile: type[Profile], amount: float) -> bool:
        r = req.get("https://run.mocky.io/v3/5794d450-d2e2-4412-8131-73d0293ac1cc")
        return r.status_code == 200 and b'Autorizado' in r.content
    
    def is_balance_enough_for_transaction(
        sender_balance: type[Decimal], 
        transaction_amount: type[Decimal]) -> bool:
        return sender_balance >= transaction_amount