class Presets(object):
    HELP_TEXT = """
EL Youtube Downloader Bot Help:

>> Send an image to setup permanent custom thumbnail.

>> To delete saved thumbnail, please select from options. 

>> If no custom thumbnail is given, bot will use the default youtube video thumbnail.

>> Use inline search for selecting video or send a youtube link to start download.

Join <a href='https://t.me/ELUpdates'>Update Channel</a> | Github <a href='https://github.com/EL-Coders'>Link</a>   
    """
    WELCOME_MSG = "Hi {},\nI'm a simple Youtube Downloader Bot.\nAlso, you can use me to search videos inline."
    OPTIONS_TXT = "I am a youtube downloader bot.\nYou can use me to search videos inline."
    RESULTS_TXT = "Search Results:"
    NO_RESULTS = "No results, change search keyword & try:"
    DESCRIPTION = "Duration: {} || {}"
    NOT_AUTH_TXT = "You are not authorised to use the bot"
    DEFAULT_TITLE = "Source Code"
    DEFAULT_THUMB_URL = "https://image.flaticon.com/icons/png/512/25/25231.png"
    DEFAULT_LINK = "https://github.com/EL-Coders/ELYoutubeBot"
    DEFAULT_DESCRIPTION = "EL-Coders - Github"
    DEV_TITLE = "Developer"
    DEV_THUMB_URL = "https://freepikpsd.com/media/2019/10/software-developer-icon-png-2-Transparent-Images.png"
    DEV_LINK = "https://t.me/CoderEL"
    DEV_DESCRIPTION = "EL Coder - Telegram"
    SHARE_BUTTON_TEXT = "Hi..  👋\nCheckout : @{username}\nFor searching & downloading & youtube videos"
    SAVED_THUMB = "<b>Thumbnail Saved Successfully</b>\n<code>This file will be used in next YouTube " \
                  "downloads until you clear it !</code> "
    WAIT_MESSAGE = "Please wait..!"
    THUMB_CAPTION = "<code>This image is your current thumbnail, Tap </code><b> DEL THUMB </b><code> if you wish to " \
                    "clear it !</code> "
    NO_THUMB = "There are no thumbnails saved, please send one !"
    DEL_THUMB_CNF = "Thumbnail cleared"
    LINK_ERROR = "Error occured !\nPlease try again later.."
    #
    #
    #
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    FINISHED_PROGRESS_STR = "◼️"
    UN_FINISHED_PROGRESS_STR = "◻️"
    CHECKING_LINK = "Checking Link.. Please wait"
    DOWNLOAD_START = "Downloading... Please wait !"
    UPLOAD_START = "Uploading to telegram..."
    NOT_DOWNLOADABLE = "URL not available !"
    CANCEL_PROCESS = "<b>Process Cancelled Successfully</b>  ✅"
    SEND_TEXT = "<b>Processing...</b>\n<i>This message will automatically disappear when the broadcasting is finished</i> "
    REPLY_ERROR = "<i>Use this command as a replay to any telegram message with out any spaces.</i>"
    USERS_LIST = "<b>Total: {}</b>\n\nSubscribers - {}\nBlocked / Deleted - {}"
    WAIT_MSG = "<b>Processing...</b>\n<i>This will take some time...</i>"
    PROMPT_THUMB = "<b>Do you want to set this image as a thumbnail?</b>"
    FORMAT_SELECTION = """
<b>Title -</b> {}
<b>Channel -</b> <a href={}>{}</a>
<b>Uploaded On -</b> {}
<b>Views -</b> {}  |  <b>Rating:</b> {}

<b>Select the desired format: 'S' for Video & 'D' for File</b>
    """
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    CUSTOM_CAPTION_UL_FILE = "\xad \xad\n<code>{}</code>\n\n<b>Join - </b><b><a href='https://t.me/ELUpdates'>@ELUpdates</a></b>"
    RCHD_TG_API_LIMIT = "Detected File Size: {}\nSorry. But, I cannot upload files " \
                        "greater than 1.95GB due to Telegram API limitations."
    AD_STRING_TO_REPLACE = "please report this issue on https://yt-dl.org/bug . Make sure you are using the " \
                           "latest version; see  https://yt-dl.org/update  on how to update. Be sure to call " \
                           "youtube-dl with the --verbose flag and include its complete output."
