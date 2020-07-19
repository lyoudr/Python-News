import React from 'react';
import AuthService from '../../services/AuthService';
import Cookie from 'js-cookie';

class Login extends React.Component {
  constructor(props) {
    super(props)
    this.username = React.createRef()
    this.password = React.createRef()
  }
  
  login(){
    const user_info = {
      'username': this.username.current.value,
      'password': this.password.current.value
    }
    AuthService.login(user_info)
      .then(res => {
        if(res.status == 'ok'){
          Cookie.set('user_id', res.user_id);
          this.props.history.push('/news');
        }
      })
  }

  render(){
    return(
      <div>
        <p>Username</p>
        <input ref={this.username} className='username'/>
        <p>Password</p>
        <input ref={this.password} className='password'/>
        <button onClick={this.login.bind(this)}>Login</button>
      </div>
    )
  }
}

export default Login