import { useQuery, gql } from '@apollo/client';

const GET_USERS = gql`
query AllUsers {
  allUsers {
    edges {
      node {
        id
        username
        email
      }
    }
  }
}
`;

function DisplayUsers() {
  const { loading, error, data } = useQuery(GET_USERS);
  
  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error. Sad Panda.</p>;

  return (
    <div>
      {data && data.allUsers.edges.map(({node}) => (
        <div key={node.id}>
          <p>{node.username}</p>
        </div>
      ))}
    </div>
  );
}

export default function App() {
  return (
    <div>
      <DisplayUsers />
    </div>
  );
}
