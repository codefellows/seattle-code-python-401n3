import Head from 'next/head'
import Link from 'next/link'
import { replies } from '../data'
import { useState } from 'react'

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

    // setReply(randomReply);
  }

  function getLastReply(){
    if (answeredQuestions.length == 0) {
      return 'Ask me anything';
    }

    return answeredQuestions[answeredQuestions.length -1].reply;

  }

  return (
    <div>
      <head>
        <title>Magic 8 Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </head>
      <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-100">
        <h1 className="text-4xl">Magic 8 Ball</h1>
        <p className="text-xl">{ answeredQuestions.length } Question Answered</p>
      </header>
      <main>
        <form onSubmit={ questionAskedHandler }className="flex w-1/2 p-2 mx-auto bg-gray-200">
          <input name="question" className="flex-auto pl-1"/>
          <button className="px-2 py-1 bg-gray-500 text-gray-100">Ask</button>
        </form>
        <div className="w-96 h-96 mx-auto my-4 bg-gray-900 rounded-full">
          <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
            <p className="text-xl text-center">{ getLastReply() }</p>
          </div>  
        </div>
        <table className="w-1/2 mx-auto my-4">
          <thead>
            <tr>
              <th className="border border-gray-700">No.</th>
              <th className="border border-gray-700">Question</th>
              <th className="border border-gray-700">Response</th>
            </tr>
          </thead>
          <tbody>
            {answeredQuestions.map(item => {
              return(<tr>
                <td className="border border-gray-700">{item.id +1}</td>
                <td className="border border-gray-700">{item.question}</td>
                <td className="border border-gray-700">{item.reply}</td>
               </tr>)
            })}

          </tbody>
        </table>
      </main>
      <footer className="p-4 bg-gray-500 text-gray-100">
        <nav className="flex items-center justify-left space-x-10">
          <Link href="/careers">
            <a className="text-xl" href="careers">Careers</a>
          </Link>
          <Link href="/aboutus">
            <a className="text-xl" href="careers">About Us</a>
          </Link>
        </nav>
      </footer>
    </div>
  )
}
