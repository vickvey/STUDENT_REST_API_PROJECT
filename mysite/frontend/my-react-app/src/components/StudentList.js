import React, { useState, useEffect } from 'react';
import axios from 'axios';

const StudentList = () => {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/api/students/')
      .then(response => {
        setStudents(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('There was an error fetching the students!', error);
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>There was an error loading the students.</p>;

  return (
    <div>
      <h1>Student List</h1>
      <ul>
        {students.length > 0 ? (
          students.map(student => (
            <li key={student.roll_number}>
              Name: {student.name}, Roll Number: {student.roll_number}, Major: {student.major}
            </li>
          ))
        ) : (
          <p>No students found.</p>
        )}
      </ul>
    </div>
  );
};

export default StudentList;
