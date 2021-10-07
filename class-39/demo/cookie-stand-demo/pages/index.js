import Head from 'next/head'
import { useAuth } from '../contexts/auth'
import useResource from '../hooks/useResource'

export default function Home() {

  const { user, login, logout } = useAuth();
  const { resources, loading, createResource, deleteResource } = useResource(); 
  // const user = { username: 'roger'};
  // const user = null;

  return (
    <div>
      <Head>
        <title>Cookie Stand Demo</title>
      </Head>

      <main className="p-4 space-y-8 text-center">
      <h1 className="text-4xl">Fetching Data from Authenticated API</h1>
                {user ? (
                    <>
                        <h2>Welcome {user.username}</h2>

                        <button onClick={logout} className="p-2 text-white bg-gray-500 rounded">Logout</button>

                        <StandCreateForm onCreate={createResource} />

                        <StandList stands={resources} loading={loading} onDelete={deleteResource}/>
                    </>
                ) : (
                    <>
                        <h2>Need to log in</h2>
                        <button onClick={() => login(process.env.NEXT_PUBLIC_USERNAME, process.env.NEXT_PUBLIC_PASSWORD)} className="p-2 text-white bg-gray-500 rounded">Login</button>
                    </>
                )}
      </main>
    </div>
  )
}

function StandList({ stands, loading, onDelete }) {

  if (loading) return <p>Loading...</p>

  return <ul>
      {stands?.map(stand => (
          <li key={stand.id} className="space-x-2">
              <span>{stand.location}</span>
              <span onClick={() => onDelete(stand.id)}>[X]</span>
          </li>
      ))}
  </ul>
}

function StandCreateForm( { onCreate }) {
  function handleSubmit(event) {
    event.preventDefault(); // Here
    const standInfo = {
      location: event.target.location.value,
      minimum_customers_per_hour: parseInt(event.target.min.value),
      maximum_customers_per_hour: parseInt(event.target.max.value),
      average_cookies_per_sale: parseFloat(event.target.average.value),
    }

    onCreate(standInfo);
    event.target.reset();
  }
  return (
    <form onSubmit={ handleSubmit }>
      <input className="border-2 border-black" name="location" placeholder="location"/>
      <input className="border-2 border-black" name="min" placeholder="min"/>
      <input className="border-2 border-black" name="max" placeholder="max"/>
      <input className="border-2 border-black" name="average" placeholder="average"/>
      <button>CREATE</button>
    </form>
  )
}