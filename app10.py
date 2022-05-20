import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('차트 그리기1')

    df = pd.read_csv('data2/iris.csv')
 
    st.dataframe(df)

    # 차트그리기
    # sepal_lenth와 sepal_width의 관계를 차트로 나타내시오.
    
    fig = plt.figure() # 여기서부턴 차트영역이다. 
    plt.scatter(data = df, x = 'sepal_length', y ='sepal_width')
    plt.title('Sepla Length vs Sepla Width')
    plt.xlabel('Sepla Length')
    plt.ylabel('Sepla Width')
    st.pyplot(fig)

    fig2 = plt.figure()
    sns.scatterplot(data = df, x = 'sepal_length', y ='sepal_width')
    plt.title('Sepla Length vs Sepla Width')
    st.pyplot(fig2)

    fig3 = plt.figure()
    sns.regplot(data = df, x = 'sepal_length', y ='sepal_width')
    st.pyplot(fig3)

    # sepal_length로 히스토그램을 그린다.
    # bin의 갯수는 20개로
    fig4 = plt.figure()
    plt.hist(data= df, x = 'sepal_length',bins=20,rwidth=0.8)
    st.pyplot(fig4)

    # sepal_length 히스토그램을 그리되, 
    # bin의 갯수를 10개와 20개로
    # 두개의 차트를 수평으로 보여주기

    fig5 = plt.figure(figsize = (10,4))
    plt.subplot(1,2,1)
    plt.hist(data= df, x = 'sepal_length',bins=10,rwidth=0.8)

    plt.subplot(1,2,2)
    plt.hist(data= df, x = 'sepal_length',bins=20,rwidth=0.8)

    st.pyplot(fig5)

    # species 컬럼의 데이터를 각각 몇개씩 있는지
    # 차트로 나타내시오

    fig6 = plt.figure()
    sns.countplot(data = df, x ='species')
    st.pyplot(fig6)

    ### 지금까지 한건, plt와 seaborn 차트를 streamlit에 그리는 방법했다.

    ## 데이터 프레임이 제공하는 차트함수도
    # streamlit에 그릴수 있다. 

    # species는 각각 몇개인지, 데이터프레임의 차트로 그리는 방법
    fig7 = plt.figure()
    df['species'].value_counts().plot(kind = 'bar')
    st.pyplot(fig7)

    # sepla_length 컬럼을 히스토그램으로!
    fig8 = plt.figure()
    df['sepal_length'].hist(bins = 40,rwidth = 0.8)
    st.pyplot(fig8)


if __name__ == '__main__':
    main()