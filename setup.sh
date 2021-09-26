mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"ankurlimbashia12@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
base=\"dark\"\n\
primaryColor=\"#f3e5e8\"\n\
backgroundColor=\"#14293b\"\n\
secondaryBackgroundColor=\"#475d87\"\n\
textColor=\"#ffffff\"\n\

" > ~/.streamlit/config.toml



