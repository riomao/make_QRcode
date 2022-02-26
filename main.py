import streamlit as st
import qrcode
from PIL import Image
import numpy as np
#qrURL = 'https://qiita.com/koikeke0911/items/a52df340836ef5661390'
#image = qrcode.make(qrURL)
#image.save('qr_code.


st.title('QRコード生成ページ')
qrURL = st.text_input("QRコードにしたいページのURLを入力してください")
if st.button("QRコードを作る"):
    _img = qrcode.make(qrURL)
    _img.save("qr_code.png")
    img = Image.open("qr_code.png")
    st.write(np.array(img).shape)
    st.image(img)
    