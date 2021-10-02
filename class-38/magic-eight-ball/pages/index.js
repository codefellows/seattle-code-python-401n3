import Head from 'next/head'
import { replies } from '../data'
import { useState } from 'react'
import Footer from '../components/footer'
import Header from '../components/header'
import QuestionForm from '../components/question-form'
import History from '../components/history'
import EightBall from '../components/eightball'

export default function Home() {

  // const [reply, setReply] = useState('Ask me anything');
  const [answeredQuestions, setAnsweredQuestions] = useState([])

  function questionAskedHandler(event){
    event.preventDefault();

    const randomReply = replies[Math.floor(Math.random() * replies.length)];

    const answeredQuestion = {
      question: event.target.question.value,
      reply: randomReply,
      id: answeredQuestions.length
    }

    console.log('answeredQuestion', answeredQuestion);
    setAnsweredQuestions([...answeredQuestions, answeredQuestion]);

  }

  // function getLastReply(){
  //   if (answeredQuestions.length == 0) {
  //     return 'Ask me anything';
  //   }
  //   return answeredQuestions[answeredQuestions.length -1].reply;
  // }

  return (
    <div>
      <head>
        <title>Magic 8 Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </head>
      <Header answerCount={answeredQuestions.length}/>
      <QuestionForm askedQues={questionAskedHandler}/>
      <EightBall getLastReply={answeredQuestions[answeredQuestions.length -1]}/>
      <History answeredQuestions={answeredQuestions}/>
      <Footer />
    </div>
  )
}
