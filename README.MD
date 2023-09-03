# VKAuth Library

VKAuth is a Python library that helps you to authenticate with VK.com using cookies from your browser. The library automatically fetches required cookies from supported browsers, establishes a session, and retrieves an access token.

## Features

- Automatic fetching of cookies from supported browsers
- Establishing a session with VK.com
- Fetching access token for user and group scopes

## Installation

Use the package manager [pip ↗](https://pip.pypa.io/en/stable/) to install VKAuth.

```bash
pip install vkauth
```

## Usage

```python
from vkauth import VKAuth

auth = VKAuth()

# to get a user token
user_token = auth.get_token()

# to get a group token
group_token = auth.get_token(group_id='your_group_id')
```

## Supported Browsers

- Google Chrome
- Yandex Browser
- Mozilla Firefox
- Microsoft Edge
- Opera
- Opera GX

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT ↗](https://choosealicense.com/licenses/mit/)

## Disclaimer
This library is intended to be used for educational purposes only. Never use it to exploit or harm someone's privacy without their consent. The maintainers of this library are not responsible for any misuse by the users.

## Contact
For any issues or suggestions, please create an issue on the GitHub repository.