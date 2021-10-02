export default function History(props){
    return(
        <table className="w-1/2 mx-auto my-4">
          <thead>
            <tr>
              <th className="border border-gray-700">No.</th>
              <th className="border border-gray-700">Question</th>
              <th className="border border-gray-700">Response</th>
            </tr>
          </thead>
          <tbody>
            {props.answeredQuestions.map(item => {
              return(<tr className="odd:bg-gray-200">
                <td className="border border-gray-700">{item.id +1}</td>
                <td className="border border-gray-700">{item.question}</td>
                <td className="border border-gray-700">{item.reply}</td>
               </tr>)
            })}

          </tbody>
        </table>
    )
}