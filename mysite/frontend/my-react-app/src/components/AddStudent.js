import React, { useState } from 'react';
import axios from 'axios';

const AddStudent = () => {
  const [name, setName] = useState('');
  const [rollNumber, setRollNumber] = useState('');
  const [major, setMajor] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('http://localhost:8000/api/students/', {
      name,
      roll_number: rollNumber,
      major
    })
    .then(response => {
      alert('Student added successfully!');
      setName('');
      setRollNumber('');
      setMajor('');
    })
    .catch(error => {
      console.error('There was an error adding the student!', error);
    });
  };

  return (
    <div>
      <h1>Add Student</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Name"
          required
        />
        <input
          type="number"
          value={rollNumber}
          onChange={(e) => setRollNumber(e.target.value)}
          placeholder="Roll Number"
          required
        />
        <input
          type="text"
          value={major}
          onChange={(e) => setMajor(e.target.value)}
          placeholder="Major"
          required
        />
        <button type="submit">Add Student</button>
      </form>
    </div>
  );
};

export default AddStudent;
