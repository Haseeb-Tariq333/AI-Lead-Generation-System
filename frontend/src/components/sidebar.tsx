import Link from "next/link";

const navItems = [{ href: "/leads", label: "Leads" }];

export function Sidebar() {
  return (
    <aside className="hidden w-60 shrink-0 border-r bg-muted/40 md:block">
      <div className="px-6 py-5">
        <span className="text-lg font-semibold">Lead Intel</span>
      </div>
      <nav className="flex flex-col gap-1 px-3">
        {navItems.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className="rounded-md px-3 py-2 text-sm font-medium hover:bg-muted"
          >
            {item.label}
          </Link>
        ))}
        <span className="rounded-md px-3 py-2 text-sm text-muted-foreground">
          New Search (Week 2)
        </span>
      </nav>
    </aside>
  );
}