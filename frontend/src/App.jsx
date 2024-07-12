import { useEffect, useState } from 'react'

import './App.css'
import ContactList from './components/ContactList'

function App() {
  const [contacts, setContacts] = usestate([])


  useEffect(() => {
    fetchContacts()
  }, [])


  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  }



  return <ContactList contacts={contacts} />
}

export default App
