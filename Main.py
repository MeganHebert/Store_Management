import Login 
import user_actions
import admin_actions
from models import CurrentUser

if __name__ == "__main__":
    current_user: CurrentUser = Login.initial_login()
    print(current_user)
    if current_user.is_admin is False:
        user_actions.home_page(current_user)
    else:
        admin_actions.admin_home_page(current_user)
