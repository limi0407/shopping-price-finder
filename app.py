import streamlit as st
from urllib.parse import quote

st.set_page_config(page_title="ショッピング検索URLジェネレーター", page_icon="🛒")

st.title("🛒 ショッピング検索URLジェネレーター")
st.write("商品名を入力すると、各ショッピングサイトの検索URLを生成します。")

st.divider()

# 商品名の入力欄
product_name = st.text_input("🔍 商品名を入力してください", placeholder="例: ワイヤレスイヤホン")

if product_name:
    # URLエンコード（日本語や空白を安全な形式に変換）
    encoded = quote(product_name)

    # 各サイトの検索URL
    amazon_url = f"https://www.amazon.co.jp/s?k={encoded}"
    rakuten_url = f"https://search.rakuten.co.jp/search/mall/{encoded}/"
    yahoo_url = f"https://shopping.yahoo.co.jp/search?p={encoded}"

    st.subheader(f"「{product_name}」の検索リンク")

    # Amazon
    st.markdown("### 🟠 Amazon")
    st.code(amazon_url)
    st.link_button("Amazonで開く", amazon_url, use_container_width=True)

    st.divider()

    # 楽天市場
    st.markdown("### 🔴 楽天市場")
    st.code(rakuten_url)
    st.link_button("楽天市場で開く", rakuten_url, use_container_width=True)

    st.divider()

    # Yahoo!ショッピング
    st.markdown("### 🟣 Yahoo!ショッピング")
    st.code(yahoo_url)
    st.link_button("Yahoo!ショッピングで開く", yahoo_url, use_container_width=True)

else:
    st.info("上の入力欄に商品名を入力してください。")
