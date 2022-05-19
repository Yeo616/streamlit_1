import streamlit as st

def main():
    st.title('웹 대시보드')
    st.text('웹 대시보드 개발기')

    name = '홍길동'

    # 제 이름은 홍길동 입니다. 
    print('제 이름은 {}입니다.'.format(name))
    st.text('제 이름은 {}입니다.'.format(name))

    st.header('이 영역은 헤더 영역')

    st.subheader('이 영역은 subheader영역')

    st.success('작업이 성공했을 때 st.success')

    st.warning('경고 문구를 보여주고 싶을 때 st.warning')

    st.info('정보를 보여주고 싶을 때 info')

    st.error('문제가 발생했을 때 st.error')

    # 파이썬 함수 사용법을 보여주고 싶을 때
    st.help(sum)
    st.help(len)







if __name__ == '__main__':
    main()

# 메인 함수에 무엇을 작성하냐에 따라서, 화면에 보여지는 것이 다르다.
