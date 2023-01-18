import React, { Component } from 'react'
import Box from '@mui/material/Box';
import PropTypes from 'prop-types';


import Todo from '../../Components/Todo/Todo';
import Weather from '../../Components/Weather/Weather';
import Boot from '../Boot/Boot'


function Item(props) {
    const { sx, ...other } = props;
    return (
      <Box
        sx={{
          color: (theme) => (theme.palette.mode === 'dark' ? 'grey.300' : 'grey.800'),
          border: '1px solid',
          borderColor: (theme) =>
            theme.palette.mode === 'dark' ? 'grey.800' : 'grey.300',
          p: 1,
          m: 1,
          borderRadius: 2,
          fontSize: '0.875rem',
          fontWeight: '700',
          ...sx,
        }}
        {...other}
      />
    );
  }
  
  Item.propTypes = {
    sx: PropTypes.oneOfType([
      PropTypes.arrayOf(
        PropTypes.oneOfType([PropTypes.func, PropTypes.object, PropTypes.bool]),
      ),
      PropTypes.func,
      PropTypes.object,
    ]),
  };


export default class Dashboard extends Component {
    render() {
        if(localStorage.getItem('token') === null){
            window.location.href = '/login';
            return console.log(localStorage.getItem('token'))
            
        }
        else if(localStorage.getItem('token') != null){
            console.log(localStorage.getItem('token'))
        
        return (
            <body>

                <Box   sx={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)' }}>
                    <Item>
                <div className='a' id="weather">
                    <Weather></Weather>
                </div>
                </Item>
                <Item>
                <div className='a' id="chat">
                    <Boot></Boot>
                </div>
                </Item>
                <Item>
                <div className='a' id="todo">
                    <Todo></Todo>
                </div>
                </Item>
                </Box>
            
                
            </body>
        )
    }
        return(            
            null
            )
}}