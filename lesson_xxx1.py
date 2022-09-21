import time
import streamlit as st

st.title("Streamlit 超入門")

#st.write("Display Image")

# if st.checkbox('Show Image'):
#     img = Image.open('sample.JPG')
#     st.image(img, caption='tartle', use_column_width=True)


#st.write("Interactive Widgets")

# option = st.selectbox(
#     "あなたが好きな数字を教えてください。",
#     list(range(1, 11))
# )
#
# "あなたの好きな数字は,", option, 'です。'

# option = st.text_input("あなたの趣味を教えてください。")
# "あなたの趣味は", option, "です。"
#
# condition = st.slider("あなたの今の調子は？", 0, 100, 50)
# "コンディション：", condition

# #サイドバー
# st.sidebar.write("Interactive Widgets")
#
# option = st.sidebar.text_input("あなたの趣味を教えてください。")
# "あなたの趣味は", option, "です。"
#
# condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
# "コンディション：", condition

#サイドバー
#st.write("Interactive Widgets")
st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)

"Done!!"
left_column, right_column = st.beta_columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.beta_expander("問い合わせ1")
expander1.write("問い合わせ1の回答を書く")
expander2 = st.beta_expander("問い合わせ2")
expander2.write("問い合わせ2の回答を書く")
expander3 = st.beta_expander("問い合わせ3")
expander3.write("問い合わせ3の回答を書く")


# option = st.text_input("あなたの趣味を教えてください。")
# "あなたの趣味は", option, "です。"
#
# condition = st.slider("あなたの今の調子は？", 0, 100, 50)
# "コンディション：", condition

#st.write("DataFrame")

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

#st.write(df)
#st.dataframe(df, width=100, height=100)
#st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))
#
# """
# # 章
# ## 節
# ### 項
#
# ```python
# import numpy as np
# import pandas as pd
# import streamlit as st
# ```
# """

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
#st.map(df)


