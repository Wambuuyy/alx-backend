import express from 'express';
import Redis from 'ioredis';

const app = express();
const port = 1245;
const redis = new Redis();

// Define products
const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  // ... add other products here
];

// Get item by ID
function getItemById(id) {
  return listProducts.find((item) => item.id === id);
}

// Reserve stock by ID
function reserveStockById(itemId, stock) {
  return redis.set(`item.${itemId}`, stock);
}

// Get current reserved stock by ID
async function getCurrentReservedStockById(itemId) {
  const stock = await redis.get(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
}

// Routes
app.get('/list_products', (req, res) => {
  const products = listProducts.map((item) => ({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
  }));
  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const id = parseInt(req.params.itemId, 10);
  const item = getItemById(id);
  if (item) {
    const reservedStock = await getCurrentReservedStockById(id);
    res.json({
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock,
      currentQuantity: item.stock - reservedStock,
    });
  } else {
    res.json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const id = parseInt(req.params.itemId, 10);
  const item = getItemById(id);
  if (item) {
    const reservedStock = await getCurrentReservedStockById(id);
    if (item.stock > reservedStock) {
      await reserveStockById(id, reservedStock + 1);
      res.json({ status: 'Reservation confirmed' });
    } else {
      res.json({ status: 'Not enough stock available' });
    }
  } else {
    res.json({ status: 'Product not found' });
  }
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
