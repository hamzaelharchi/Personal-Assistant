import React, { Component } from 'react'
import { Form, Button, Container } from 'react-bootstrap'
const axios = require('axios')



export default class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            email: '',
            password: '',
            first_name: '',
            last_name: '',
            id:'',
        };
        this.onChange = this.onChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    onChange = (e) => this.setState({ [e.target.name]: e.target.value });
    handleSubmit(event) {
        axios.post('http://localhost:8000/account/api/token/',{
            username: this.state.email,
            password: this.state.password,
        }).then(function (res){
            // convert from string to obj (JSON)
            console.log("DATA :")
            let obj = JSON.parse(res.config.data);
            console.log(typeof(obj))
            console.log(obj)
            localStorage.setItem('token', res.data.access);
            localStorage.setItem('user',  res.config.data);
            window.location.href = '/dashboard';

        }).catch(function (err){
            if (err.response) {
                if(err.response.statusText === "Bad Request"){
                    alert("The E-mail and Password fields are required")
                }else{
                    alert("Please enter a correct E-mail or Password")
                }
                // Request made and server responded
                console.log(err.response.status);
                console.log(err.response.data.password)
                console.log(err.response.data.detail)
                console.log(err.response.statusText)
              }else {
                // Something happened in setting up the request that triggered an Error
                console.log('Error', err.message);
              }
        })
        event.preventDefault();
    }
    render() {
        return (
            <Container style={{ marginTop: '150px' }}>
                <Form style={{ color: 'white' }} className="d-flex flex-column align-items-center">
                    <Form.Group controlId="formBasicEmail" style={{ width: '300px' }}>
                        <Form.Label>Email address</Form.Label>
                        <Form.Control type="email" placeholder="Enter email" name="email" value={this.state.email} onChange={this.onChange}/>           
                    </Form.Group>
                    
                    <Form.Group controlId="formBasicPassword" style={{ width: '300px' }}>
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Password" name="password" value={this.state.password} onChange={this.onChange}/>
                    </Form.Group>
                    
                    <Form.Group controlId="formBasicCheckbox" className="flex-start" style={{ marginLeft: '-180px' }}>
                            <Form.Check type="checkbox" label="Check me out" />
                    </Form.Group>
                    
                    <Button variant="primary" type="submit" onClick={this.handleSubmit} className="btn-block" style={{ maxWidth: '300px' }}>
                        Submit
                    </Button>   
                </Form>
            </Container>
            
        )
    }
}