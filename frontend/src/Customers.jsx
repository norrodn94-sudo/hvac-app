import React, {useEffect, useState} from 'react'

export default function Customers(){
  const [customers, setCustomers] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(()=>{
    fetch('/customers/')
      .then(r=>r.json())
      .then(data=>{
        setCustomers(data)
        setLoading(false)
      })
      .catch(()=>setLoading(false))
  },[])

  if(loading) return <div>Loading...</div>
  return (
    <div style={{padding:20}}>
      <h2>Customers</h2>
      <table style={{width:'100%',borderCollapse:'collapse'}}>
        <thead>
          <tr><th style={{textAlign:'left'}}>Name</th><th>Email</th><th>Phone</th></tr>
        </thead>
        <tbody>
          {customers.map(c=> (
            <tr key={c.id} style={{borderTop:'1px solid #eee'}}>
              <td>{c.name}</td>
              <td>{c.email || '-'}</td>
              <td>{c.phone || '-'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
