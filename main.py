import streamlit as st

# タイトル
st.title('あなたの情報をいれてください')

# メインエリアの入力フィールド
num_units = st.number_input('戸数', min_value=0, value=50)
manager_hours = st.number_input('管理員の月間の派遣時間', min_value=0, value=100)
cleaner_hours = st.number_input('清掃員の月間の派遣時間', min_value=0, value=30)
cleaning_count = st.number_input('定期清掃の実施回数', min_value=0, value=1)
elevator_count = st.number_input('エレベーターの数', min_value=0, value=1)
pipe_cleaning_count = st.number_input('雑排水管洗浄の実施回数', min_value=0, value=1)
has_reservoir = st.checkbox('貯水槽があればチェック', value=False)
has_rooftop_reservoir = st.checkbox('屋上貯水槽があればチェック', value=False)


# サイドバーの入力フィールド
st.sidebar.title('ここに設定を入力します')
unit_price = st.sidebar.number_input('事務官単価（戸数×単価）', min_value=0, value=2500)
manager_rate = st.sidebar.number_input('管理員の時間単価 (円)', min_value=0, value=2000)
cleaner_rate = st.sidebar.number_input('清掃員の時間単価 (円)', min_value=0, value=2000)
cleaning_cost = st.sidebar.number_input('定期清掃の費用 (円、年間)', min_value=0, value=100000)
elevator_cost = st.sidebar.number_input('エレベーターの費用 (円、年間)', min_value=0, value=70000)
pipe_cleaning_cost = st.sidebar.number_input('雑排水管洗浄の費用 (戸数×円、年間)', min_value=0, value=5000)
reservoir_cost = st.sidebar.number_input('貯水槽の追加費用 (円、年間)', min_value=0, value=80000)
rooftop_reservoir_cost = st.sidebar.number_input('屋上貯水槽の追加費用 (円、年間)', min_value=0, value=80000)

# 計算
total_cost = (
    (num_units * unit_price) +
    (manager_hours * manager_rate) +
    (cleaner_hours * cleaner_rate) +
    (cleaning_count * cleaning_cost / 12) +
    (elevator_count * elevator_cost / 12) +
    (pipe_cleaning_count * num_units * pipe_cleaning_cost / 12) +  # 12で割る
    (reservoir_cost / 12 if has_reservoir else 0) +  # 12で割る
    (rooftop_reservoir_cost / 12 if has_rooftop_reservoir else 0)  # 12で割る
)

# 結果表示
st.write(f'合計: {total_cost:,.0f} 円')
