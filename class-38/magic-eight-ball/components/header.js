export default function Header(props) {
    return(
        <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-100">
            <h1 className="text-4xl">Magic 8 Ball</h1>
            <p className="text-xl">{ props.answerCount } Question Answered</p>
        </header>
    )
}