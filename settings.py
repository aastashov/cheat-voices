from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKEN')

URL_VOTES = 'http://travelshop.kg/votes'
URL_REGISTER = 'http://travelshop.kg/post/register'
URL_LOGIN = 'http://travelshop.kg/post/login'
URL_LIKE = 'http://travelshop.kg/toggleLike'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
CONTENT_TYPE = 'application/x-www-form-urlencoded; charset=UTF-8'
HEADERS = {
    'Content-Type': CONTENT_TYPE,
    'User-Agent': USER_AGENT,
}
