def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxf9be6b10162d442d97efadbc134ecb04.mailgun.org/messages",
        auth=("api", "0913e665871018d0accf8a564bfe72e7-28e9457d-c7122ac6"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxf9be6b10162d442d97efadbc134ecb04.mailgun.org>",
              "to": "Amin Soltani <aminsoltani.1221@gmail.com>",
              "subject": "Hello Amin Soltani",
              "text": "Congratulations Amin Soltani, you just sent an email with Mailgun!  You are truly awesome!"})


send_simple_message()
