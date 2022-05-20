import streamlit as st
import pandas as pd

import altair as alt
# 따로 설치를 안해도 되는 이유는: 스트림릿을 설치할 떄, 딸려온다. 

import plotly.express as px

def main():
    # 스트림릿에서 제공해주는 차트
    # line_chart, area)chart

    df1 = pd.read_csv('data2/lang_data.csv')
    st.dataframe(df1)

    lang_list = df1.columns[1:]
    
    choice_list = st.multiselect('언어를 선택해주세요', lang_list)

    if len(choice_list) != 0:
        df_choice = df1[choice_list]

        st.dataframe(df_choice)

        # 스트림릿이 제공하는 line_chart
        st.line_chart(df_choice)

        # 스트림릿이 제공하는 area_chart
        st.area_chart(df_choice)

    df2 = pd.read_csv('data2/iris.csv')
    
    # 스트림릿이 제공하는 bar_chart
    st.bar_chart(df2.iloc[:,0:-2+1])

    ## 웹에서 사용할 수 있는 차트 라이브러리 중
    ## Altair 차트 

    alt_chart = alt.Chart(df2).mark_circle().encode(
        x = 'petal_length',
        y = 'petal_width',
        color = 'species'
    )
    # mark관련 차트를 이용할 수 있다. 상황에 따라서 이용해보자. 

    # 라이브러리이기 때문에 스트림릿에서 그려줘야한다. 
    # altair 차트는 내가 그려줄게, 그러니까, 너는 변수를 집어넣어.. 라는 뜻
    st.altair_chart(alt_chart)

    ## 스트림릿의 map 차트
    df3 = pd.read_csv('data2/location.csv', index_col=0)
    st.dataframe(df3)
    # 위도,경도 데이터는 지도로 표시한다. 

    # 맵 함수가 바로 있다.
    st.map(df3)

    # plotly 라이브러리를 이용한 차트 그리기
    # 스트림릿이 이미 얘를 설치해놨다.
    df4 = pd.read_csv('data2/prog_languages_data.csv', index_col=0 )
    st.dataframe(df4)

    # plotly의 pie차트
    # 쌤 회사에서 많이 쓰고 있는 것. 
    fig1 = px.pie(df4,names = 'lang',values = 'Sum',title = '각 언어별 파이차트')
    st.plotly_chart(fig1)

    # plotly의 bar차트
    df4_sorted = df4.sort_values('Sum',ascending=False)
    fig2 = px.bar(df4_sorted, x = 'lang',y='Sum')
    st.plotly_chart(fig2)


    # 주피터 노트북으로 코드를 짜고, 본다음에, 여기서 실행시키는 것.
    # vscode에서는 보기 힘드니까.


if __name__ == '__main__':
    main()



