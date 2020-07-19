const AuthService = {
  login(user_info){
    const req_info = {
      body: JSON.stringify(user_info),
      method: 'POST',
    }
    return fetch(`${process.env.REACT_APP_HOSTURL}/loginpage/`, req_info)
      .then(res => res.json())
  }
}

export default AuthService;