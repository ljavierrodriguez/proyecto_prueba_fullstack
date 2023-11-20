const getState = ({ getStore, getActions, setStore }) => {
    return {
        store: {
            apiURL: 'http://127.0.0.1:5000',
            users: null,
        },
        actions: {
            getUsers: () => {

                const { apiURL } = getStore();

                const url = `${apiURL}/api/users`
                const options = {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }

                fetch(url, options)
                    .then(response => response.json())
                    .then(datos => {
                        console.log(datos)
                        setStore({ users: datos })
                    })
            }
        }
    }
}

export default getState