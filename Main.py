import Login 
import user_actions
import admin_actions
import logging
from models import CurrentUser

if __name__ == "__main__":
    logging.basicConfig(filename="Wild_Bear.log", level=logging.DEBUG, format='%(asctime)s :: %(message)s')
    current_user: CurrentUser = Login.initial_login()
    if current_user.is_admin is False:
        user_actions.home_page(current_user)
    else:
        admin_actions.admin_home_page(current_user)
