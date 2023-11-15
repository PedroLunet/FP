// Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQDWmRwDM6J7bbd0TvauU7JuHkkK4M9RTDmuCRACM4AnbuXSbGc9tp-aJXOOs_LjTTv7-k2xNTrCf9G0gH7PYkVeqc1l3PcBruoePlpK3WcVrVJD1NSDOF2QjpKtbMO8z2JLRekcu-kGjcxGECIEXbCwbXsqYgytL8wZO2bbhPW44t9nACUTJzXyrSHtGW6X-JMiAAiYM8-0f2biq8cSXeOrnMqha7_2EEuKzhNf1kWdZju92rsSoHpuFTKmrFe94nuRMIjbpg-h9S6diwIn9e3d';
async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body:JSON.stringify(body)
  });
  return await res.json();
}

async function getTopTracks(){
  // Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
  return (await fetchWebApi(
    'v1/me/top/tracks?time_range=short_term&limit=5', 'GET'
  )).items;
}

const topTracks = await getTopTracks();
console.log(
  topTracks?.map(
    ({name, artists}) =>
      `${name} by ${artists.map(artist => artist.name).join(', ')}`
  )
);