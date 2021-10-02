import Link from 'next/link'

export default function Footer() {
    return(
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
    )
}