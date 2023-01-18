import './Todo.css';
import React from 'react';
import SendIcon from '@mui/icons-material/Send';
import { Button} from 'react-bootstrap';





class Todo extends React.Component {
    constructor(props){
      super(props);
        this.state = {
          todoList:[],
          activeItem:{
            id:null, 
            title:'',
            completed:false,
            user:null,
          },
          editing:false,
          result:'',
          u:''
        }
        this.fetchTasks = this.fetchTasks.bind(this)
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.fetchUsers = this.fetchUsers.bind(this)

  
        this.startEdit = this.startEdit.bind(this)
        this.deleteItem = this.deleteItem.bind(this)
        this.strikeUnstrike = this.strikeUnstrike.bind(this)
    };
  
  
    componentWillMount(){
      this.fetchUsers()


    }
    componentDidUpdate(pp,ps,ss){
      if(this.state.u != ps.u){
        this.fetchTasks()
      }
      


    }
  
    fetchUsers(){
      console.log('Fetching...')
  
      fetch('http://localhost:8000/account/api/users/')
      .then(response => response.json())
      .then(data => 
        this.setState({u:data.id},
          console.log(data.id))
        
        )
        
    }
    fetchTasks(){
      console.log('Fetching...')
      
      fetch(`http://127.0.0.1:8000/Home/api/tasks/${ this.state.u}/`)
      .then(response => response.json())
      .then(data => 
        this.setState({
          todoList:data
        }),
        console.log(this.state.todoList)
        
        )
        
    }
  
    handleChange(e){
      var name = e.target.name
      var value = e.target.value
      console.log('Name:', name)
      console.log('Value:', value)
  
      this.setState({
        activeItem:{
          ...this.state.activeItem,
          title:value,
          user:this.state.u
        }
      })
    }
  
    handleSubmit(e){
      e.preventDefault()
      console.log('ITEM:', this.state.activeItem)
      //var csrftoken = this.getCookie('csrftoken')
      var that=this
      var url = 'http://127.0.0.1:8000/Home/api/task-create/'
  
      if(this.state.editing === true){
        url = `http://127.0.0.1:8000/Home/api/task-update/${ this.state.activeItem.id}/`
        this.setState({
          editing:false
        })
      }
  
  
  
      fetch(url, {
        method:'POST',
        headers:{
          'Content-type':'application/json',
          //'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify(this.state.activeItem)
      }).then((response)  => {
          let r=response.json()
          
          r.then(function(data) { console.log(data)})
          this.fetchTasks()
          this.setState({
             activeItem:{
            id:null, 
            title:'',
            completed:false,
            user:null,
            u:null
          }
          })
      }).catch(function(error){
        console.log('ERROR:', error)
      })
    }


  
    startEdit(task){
      this.setState({
        activeItem:task,
        editing:true,
      })
    }
  
  
    deleteItem(task){
      //var csrftoken = this.getCookie('csrftoken')
  
      fetch(`http://127.0.0.1:8000/Home/api/task-delete/${task.id}/`, {
        method:'DELETE',
        headers:{
          'Content-type':'application/json',
          //'X-CSRFToken':csrftoken,
        },
      }).then((response) =>{
  
        this.fetchTasks()
      })
    }
  
  
    strikeUnstrike(task){
  
      task.completed = !task.completed
      var url = `http://127.0.0.1:8000/Home/api/task-update/${task.id}/`
  
        fetch(url, {
          method:'POST',
          headers:{
            'Content-type':'application/json',
            //'X-CSRFToken':csrftoken,
          },
          body:JSON.stringify({'completed': task.completed, 'title':task.title})
        }).then(() => {
          this.fetchTasks()
        })
  
      console.log('TASK:', task.completed)
    }
  
  
    render(){
      var tasks = this.state.todoList
      var self = this
{console.log(this.state.u)}
      return(
          <div className="container">
  
            <div id="task-container">
                <div  id="form-wrapper">
                   <form onSubmit={this.handleSubmit}  id="form">
                      <div className="flex-wrapper">
                          <div style={{flex: 6}}>
                              <input onChange={this.handleChange} className="form-control" id="title" value={this.state.activeItem.title} type="text" name="title" placeholder="Add task.." />
                           </div>
  
                           <div style={{flex: 1}}>
                              <input id="submit" className="btn btn-warning" value='Add Task' type="submit" name="Add" />
                            </div>
                            
                        </div>
                  </form>
               
                </div>
  
                <div  id="list-wrapper">         
                      {tasks.map(function(task, index){
                        return(
                            <div key={index} className="task-wrapper flex-wrapper">
  
                              <div onClick={() => self.strikeUnstrike(task)} style={{flex:7}}>
  
                                  {task.completed === false ? (
                                      <span>{task.title}</span>
  
                                    ) : (
  
                                      <strike>{task.title}</strike>
                                    )}
    
                              </div>
  
                              <div style={{flex:1}}>
                                  <button onClick={() => self.startEdit(task)} className="btn btn-sm btn-outline-info">Edit</button>
                              </div>
  
                              <div style={{flex:1}}>
                                  <button onClick={() => self.deleteItem(task)} className="btn btn-sm btn-outline-dark delete">-</button>
                              </div>
  
                            </div>
                          )
                      })}
                </div>
            </div>
            
          </div>
        )
    }
  }
  
  export default Todo;
