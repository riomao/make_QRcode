# make_QRcode
streamlitを使ってQRコードを生成するディレクトリです。

import streamlit as st
import qrcode
from PIL import Image
import numpy as np

st.title('QRコード生成ページ')
qrURL = st.text_input("QRコードにしたいページのURLを入力してください")
if st.button("QRコードを作る"):
    _img = qrcode.make(qrURL)
    _img.save("qr_code.png")
    img = Image.open("qr_code.png")
    st.write(np.array(img).shape)
    st.image(img)
