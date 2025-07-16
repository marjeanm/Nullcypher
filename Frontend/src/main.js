const injectComponent = async (id, path) => {
  const res = await fetch(path);
  const html = await res.text();
  document.getElementById(id).innerHTML = html;
};

injectComponent("memory-feed", "/src/components/MemoryFeed.html");
injectComponent("council-display", "/src/components/CouncilPanel.html");
