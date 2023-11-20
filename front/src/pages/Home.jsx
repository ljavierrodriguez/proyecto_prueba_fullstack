import React, { useContext, useEffect } from 'react'
import { Context } from '../store/AppContext'

const Home = () => {

    const { store, actions } = useContext(Context);

    useEffect(() => {
        actions.getUsers();
    }, [])

    return (
        <div>Home</div>
    )
}

export default Home