/*eslint-disable*/
import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  let [글제목,글제목변경] = useState(['남자코트 추천','강남 우동 맛집','파이썬 독학']);
  let [따봉,따봉변경] = useState(0);
  let posts = '강남 고기 맛집'
 
//  function 제목바꾸기(){
//   var newArray = [...글제목];
//    newArray[0] = '여자코트 추천';
//    글제목변경(newArray);
//  }

  return (
    <div className="App">
      <div className="black-nav">
        개발 Blog
      </div>
      <div className="list">
        <h4>{글제목[0]} <span onClick={()=>{따봉변경(따봉+1)}}>👍</span> {따봉}</h4>
        <p>2월 17일 발행</p>
        <hr/>
      </div>
      <div className="list">
        <h4>{글제목[1]}</h4>
        <p>2월 18일 발행</p>
        <Modal title={글제목[1]}></Modal>
        <hr/>
      </div>
      <div className="list">
        <h4>{글제목[2]}</h4>
        <p>2월 19일 발행</p>
        <hr/>
      </div>
    </div>
  );
}

function Modal(props){
  return(
    <div className='modal'>
        <h3>{props.title}</h3>
        <p>날짜</p>
        <p>상세내용</p>
    </div>
  )
}
export default App;
