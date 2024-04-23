/*eslint-disable*/
import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';

function App() {
  let [글제목,글제목변경] = useState(['남자코트 추천','강남 우동 맛집','파이썬 독학']);
  let [따봉,따봉변경] = useState([0,0,0]);
  let [modal, setModal] = useState(false);
  let [title, setTitle] = useState(0);
  let [입력값, 입력값변경] = useState('');
//  function 제목바꾸기(){
//   var newArray = [...글제목];
//    newArray[0] = '여자코트 추천';
//    글제목변경(newArray);
//  }

  return (
    <div className="App">
      <div className="black-nav">
        <h4>ReactBlog</h4>
      </div>
      {/* <div className="list">
        <h4>{글제목[0]} <span onClick={()=>{따봉변경(따봉+1)}}>👍</span> {따봉}</h4>
        <p>2월 17일 발행</p>
       
      </div>
      <div className="list">
        <h4>{글제목[1]}</h4>
        <p>2월 18일 발행</p>
      </div>
      <div className="list">
        <h4 onClick={()=>{setModal(!modal)}}>{글제목[2]}</h4>
        <p>2월 19일 발행</p>
      </div> */}
      {
        글제목.map(function(a, i){ 
          return (
            <div className="list" key={i}>
              <h4 onClick={()=>{setModal(true); setTitle(i);}}>{ 글제목[i] }
                <span onClick={(e)=>{
                  e.stopPropagation;
                  let cpy = [...따봉];
                  cpy[i] = cpy[i]+1;
                  따봉변경(cpy);
                }}>👍</span> {따봉[i]}</h4>
              <p>2월 18일 발행</p>
              <button onClick={()=>{
                let cpy = [...글제목];
                cpy.splice(i,1);
                글제목변경(cpy);
              }}>삭제</button>
            </div>  
          )
        })
      }

      <input onChange={(e)=>{ 
        입력값변경(e.target.value)
        // console.log(입력값)
        }}/>
      <button onClick={()=>{
        let cpy = [...글제목];
        cpy.unshift(입력값);
        글제목변경(cpy);
        }}>확인</button>
      {
        modal == true ? <Modal title={title} 글제목={글제목}/> : null
      }
      <Modal2></Modal2>
    </div>
  );
}

function Modal(props){
  return(
    <div className='modal'>
        <h3>{props.글제목[props.title]}</h3>
        <p>날짜</p>
        <p>상세내용</p>
        <button>글수정</button>
    </div>
  )
}

class Modal2 extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      name : 'kim',
      age : 20
    }
  }
  render(){
    return (
      <div>안녕 {this.state.age}
        <button onClick={()=>{
          this.setState({age : 21})
        }}>버튼</button>
      </div>
    )
  }
}
export default App;
