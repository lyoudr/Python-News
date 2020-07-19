import React, {lazy, Suspense} from 'react';
import { Route, Switch, BrowserRouter, Redirect } from 'react-router-dom';
import './App.css';

// Lazy Loading
const Login = lazy(() => import('./content/login/Login'));
const News = lazy(() => import('./content/news/News'));

class App extends React.Component {
  constructor(props){
    super(props)
  }
  render(){
    return(
      <Suspense fallback={'Loading...'}>
        <BrowserRouter>
          <Switch>
            <Route path="/login" component={Login}/>
            <Route path="/news" component={News}/>
          </Switch>
        </BrowserRouter>
      </Suspense>
    )
  }
}

export default App;
