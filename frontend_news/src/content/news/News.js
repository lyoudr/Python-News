import React from 'react';
import HttpService from '../../services/HttpService';

class News extends React.Component {
  constructor(props){
    super(props)
  }
  componentDidMount(){
    console.log('init')
    HttpService.get_news('music')
      .then(res => console.log('res is =>', res))
  }
  render(){
    return(
      <div>News</div>
    )
  }
}

export default News;