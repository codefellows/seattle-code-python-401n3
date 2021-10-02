export default function QuestionForm(props) {
    return(
        <form onSubmit={ props.askedQues }className="flex w-1/2 p-2 mx-auto bg-gray-200">
          <input name="question" className="flex-auto pl-1"/>
          <button className="px-2 py-1 bg-gray-500 text-gray-100">Ask</button>
        </form>
    )
}